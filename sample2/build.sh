#!/bin/sh
rm -rf ./build
echo Build Begin
echo PYTHON_3_5_EXE=$PYTHON_3_5_EXE
$PYTHON_3_5_EXE setup.py bdist_wheel --dist-dir dist/py_3_5
echo PYTHON_3_5_EXE=$PYTHON_3_5_EXE
echo Build End

echo Build Begin
echo PYTHON_3_6_EXE=$PYTHON_3_6_EXE
$PYTHON_3_6_EXE setup.py bdist_wheel --dist-dir dist/py_3_6
echo PYTHON_3_6_EXE=$PYTHON_3_6_EXE
echo Build End

#sudo -H /opt/anaconda3/envs/python_3_5/bin/pip install --upgrade --force-reinstall dist/py_3_5/*.whl
#sudo -H /opt/anaconda3/envs/python_3_6/bin/pip install --upgrade --force-reinstall dist/py_3_6/*.whl
