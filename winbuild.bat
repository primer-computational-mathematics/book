setlocal
set PYTHONUTF8=1
python scripts/generate_new_toc.py
cd _tmp
jupyter book build .
endlocal
