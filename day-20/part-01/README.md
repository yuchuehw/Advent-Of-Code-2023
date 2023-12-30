# Advent of Code 2023 - Day 20, Part 1

## Problem Statement

This task involves simulating a circuit and counting the high and low pulses when a button is pressed 1000 times.

## `simulate_circuit.py`

### Description

The `simulate_circuit.py` script reads a circuit layout from an input file and simulates the circuit's behavior after pressing the button 1000 times. The circuit consists of various components, including a broadcaster, flip-flops, and a conjunction. The script tracks the high and low pulses at each step of the simulation and calculates the final area based on the accumulated counts.

### Usage

```bash
python simulate_circuit.py
```

Replace `simulate_circuit.py` with the actual name of your Python script.

### Input

The input is read from a file named `input.txt`. Each line of the file represents a component in the circuit and its connections.

Example input file:
```
&ff -> broadcaster
broadcaster -> output
```

### Output

The script will output the calculated area of the circuit, considering the high and low pulses after 1000 button presses.

### Approach

The script follows a DFS-like simulation of the circuit, updating the signals at each component based on its type. It employs cycle detection to optimize the simulation, identifying repeating patterns in the circuit layout. The final area is then calculated based on the accumulated high and low pulses.
