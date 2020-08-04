# Dakota

The dakota project provides software for optimisation and uncertainty quantification. 

Dakota can be used for a broad range of computational tasks as it enables design exploration, risk analysis, model calibration, and quantification of margins and uncertainty with computational models.

The intended use of Dakota is to aid computational methods developed to better understand the complex physical systems they simulate. In many cases these simulations are used to find the optimal design of a system, or to make prediction for systems that can not be directly tested. 

The use of these computational simulations can lead to better system designs and improved overall performance. Furthermore, a reduced dependence on physical testing can reduce development costs and quicken the design process.

In this notebook I will summarise how the Dakota library is used to automatize the parameter space investigated in a given computational model using python.

## Installation

Dakota can be downloaded from https://dakota.sandia.gov/download.html. For the latest release savethe tar.gv file to downloads and extract it. Make sure the file is the source code. This will be yourDakota installation directory.

Before attempting to install dakota you must ensure you have the packages cmake and libboost in-stalled. If you dont you will have to find someone with the necessary admin rights to install these.

To extract the tar.gv file navigate to the file and type the following:

<p style="background:black">
<code style="background:black;color:white">tar xvzf file.tar.gz
</code>
</p>

Once the file has been extracted, navigate to the unzipped Dakota source code and find the first foldercontaining a CMakeList.txt file. Once there type the following to access cmake:

<p style="background:black">
<code style="background:black;color:white">mkdir build <br>cd build<br>ccmake ..</code>
</p>

On the window which appears,press the c key to run configure once. Once configured scroll to CMAKE-INSTALL-PREFIX and edit the variable to something memorable. (e.g /home/name/dakota) Pressthe c key again to configure and then the g key to exit back to the terminal.

Once back in the terminal type the following to run dakota:

<p style="background:black">
<code style="background:black;color:white">make -j4 <br>make install</code>
</p>

## Python template for Dakota

To automatize the parameter space in your model using Dakota you first need to have a python script in which Dakota can adjust the parameters in the model simulations. To do this create a .py file by typing the following in the terminal.

<p style="background:black">
<code style="background:black;color:white">gedit file.py
</code>
</p>

Any parameter that is meant to be changed by Dakota, needs to be put in '{ }' brackets. Dakota will evaluate changes in the response functions - print statements. In this case the print statement will be Parameter 1 and Parameter 2. This is implemented by the following:

```python
Parameter1 = {par1}
Parameter2 = {par2}
```

Dakota can automatize more parameters for more complex studies.

## Dakota bash file

The purpose of the bash file is to allow Dakota to investigate the selected parameters in the python file. In this case the bash file, e.g file.sh, creates a copy of the python file (the template file) and using the built in function ’dprepro’ changes the values of these parameters. It then runs the python script and returns the results. 

In the following bash file ’file.py’ is the previously created python file and ’file_temp.in’ is the template file.

```
#!/bin/sh
# $1 is params.in FROM Dakota
# $2 is results.out returned to Dakota
#--------------
#PRE-PROCESSING
#--------------
echo entered shell script
dprepro $1 file.py file_temp.in
echo dprepro finished
# --------
# ANALYSIS
# --------
python file_temp.in > results.tmp
# ---------------
# POST-PROCESSING
# ---------------
mv results.tmp $2
```

## Dakota input file

The Dakota input file must consist of the following blocks: environment, method, model, variables, interface and responses. Details on these blocks can be found on the Reference Manual and User’s Manual. These can be downloaded from https://dakota.sandia.gov/documentation.html.

As an exampple in this simple case Dakota puts values ranging between 1 and 2 instead of Parameter1 ’par1’, and values ranging between 3 and 4 instead of Parameter2 ’par2’ in the template. Then, Dakota prints out the response function according to the input parameter into the tabular file ’file.dat’.

```
environment
    tabular_data
        tabular_data_file = ’file.dat’
        
method
    efficient_global
        max_iterations 50
        convergence_tolerance 1e-3
        x_conv_tol 1e-3
        gaussian_process
            surfpack
        export_approx_points_file ’file_surrogate.dat’ #interpolates results for points within the
                                                       #parameter space that have not been calculated
                                                       
variables
    continuous_design = 2 #number of parameters
        initial_point   1.5 3.5
        lower_bounds   1 3
        upper_bounds   2 4
        descriptors   ’par1’ ’par2’
        
model
    single
    
interface
    fork
        analysis_driver = ’file.sh’ # bash file that connects Dakota and Python files
    deactivate evaluation_cache restart_file
    failure_capture continuation

responses
    objective_functions = 1
        sense ’maximize’
        descriptors ’max_power’ #prints the average power with the aim of finding the max average power
    no_gradients
    no_hessians
    
```

Once the python, bash and input files have been created you can run the simulation with dakota usingthe following command line:

```
dakota -i file.in -o file.out
```

## References
* https://dakota.sandia.gov