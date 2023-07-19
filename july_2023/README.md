# Tests with ChatGPT conducted in April 2023 (GPT 3.5 model)

Author: Leandro Carísio Fernandes

This repository contains tests with ChatGPT in the context of computational electromagnetics.

## 1. Translate code from MATLAB to Python

### Run 1

1. Chat [transcription](./chats/1_conversion_fdtd3_matlab_to_python_run_1.txt) and [screenshots](./chats/1_conversion_fdtd3_matlab_to_python_run_1.md)
2. [Original MATLAB code](./code/1_matlab_to_python/run%201/%5Boriginal%5D%20fdtd_3D_demo.m)
3. [Converted Python code](./code/1_matlab_to_python/run%201/%5Bconverted_chatgpt%5D%20fdtd_3D_demo.py)
4. [Converted Python code - manually adjusted](./code/1_matlab_to_python/run%201/%5Badjusted%5D%20fdtd_3D_demo.py)

### Run 2

1. Chat [transcription](./chats/1_conversion_fdtd3_matlab_to_python_run_2.txt) and [screenshots](./chats/1_conversion_fdtd3_matlab_to_python_run_2.md)
2. [Original MATLAB code](./code/1_matlab_to_python/run%202/%5Boriginal%5D%20fdtd_3D_demo.m)
3. [Converted Python code](./code/1_matlab_to_python/run%202/%5Bconverted_chatgpt%5D%20fdtd_3D_demo.py)
4. [Converted Python code - manually adjusted](./code/1_matlab_to_python/run%202/%5Badjusted%5D%20fdtd_3D_demo.py)

## 2. Writing code

### 2.1 Neural network to predict path loss

1. Chat [transcription](./chats/2_nn_path_loss_900_mhz.txt) and  and [screenshots](./chats/2_nn_path_loss_900_mhz.md)
2. [Generated Python code](./code/2_nn_pl_900mhz/script_nn.py)
4. [Generated Python code - manually adjusted](./code/2_nn_pl_900mhz/adjusted_script_nn.py)

### 2.2 MoM to calculate the radiation pattern of a dipole

1. Chat [transcription](./chats/3_mom_dipole.txt) and [screenshots](./chats/3_mom_dipole.md)
2. [Generated Python code](./code/3_mom_dipole/%5Bgenerated_chatgpt%5D%20mom_dipole.py)
3. [Generated Python code - manually adjusted](./code/3_mom_dipole/%5Badjusted%5D%20mom_dipole.py)

## 3. Code explanation

### 3.1 Explaining the FDTD-3D code a rectangular PEC

1. Chat [transcription](./chats/4_pec_rectangular_answer.txt)  and [screenshots](./chats/4_pec_rectangular_answer.md)
2. [RectangularPECSheetFDTDCore.cpp](https://github.com/carisio/emstudio/blob/master/EMStudio/src/emstudio/core/engine/fdtd/elementcore/RectangularPECSheetFDTDCore.cpp)

### 3.2 Explaining the FDTD-3D main loop to update the E-field

1. Chat [transcription](./chats/5_fdtd_loop_e_field_changed.txt) and [screenshots](./chats/5_fdtd_loop_e_field_changed.md)
2. [FDTDData.cpp](https://github.com/carisio/emstudio/blob/master/EMStudio/src/emstudio/core/engine/fdtd/FDTDData.cpp)

### 3.3 Optimization of two consecutive nested loops

1. Chat [transcription](./chats/6_optimization_two_consecutive_nested_loops.txt) and [screenshots](./chats/6_optimization_two_consecutive_nested_loops.md)