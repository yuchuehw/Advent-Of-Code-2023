"""
Advent of Code 2023 - Day 20, Part 1

Task: Circuit simulation. count the high and low pulses when button is pressed 1000 times.
"""

from collections import namedtuple
import time

def simulate_circuit(file_path: str) -> int:
    """
    Build and simulate circuit after 1000 button press.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - int: The sum of custom hash values.
    """
    with open(file_path, "r", encoding="utf8") as file:
        circuit_layout = {"button":(0,('broadcaster',))}
        # 0 = broacaster/button always send low.
        # 1 = flipflop off. send high when receive low. ignore high. (default)
        # 2 = flipflop on. send low when receive low. ignore high.
        # 3 = conjunction. update input memory then if all remembered input is high, send low. else send high
        circuit_symbol_to_int = {"%":1, "&":3}
        conjun_mem = {}
        for line in file.readlines():
            component, next_ = line.strip().split(" -> ")
            if component == 'broadcaster':
                comp_type, comp_name = 0, component
            else:
                comp_type, comp_name = circuit_symbol_to_int[component[0]], component[1:]
            
            next_ = tuple(next_.split(", "))
            
            circuit_layout[comp_name] = (comp_type, next_)
            if comp_type == 3:
                conjun_mem[comp_name] = {}

        for conjun in conjun_mem:
            for comp, comp_type_next in circuit_layout.items():
                if conjun in comp_type_next[1]:
                    conjun_mem[conjun][comp] = 0

        print(conjun_mem)
        cycle_detection = {tuple(circuit_layout.items()):(0,(0,0))}
        click_to_circ = {0:tuple(circuit_layout.items())}
        # DFS
        
        final_gen = []
        NUM_OF_CLICKS = 10000
        for click in range(NUM_OF_CLICKS):
            # print(click)
            low = 0
            high = 0
            this_gen = []
            next_gen = [("button",0,None)]
            # print()
            while next_gen:
                # print(next_gen)
                this_gen = next_gen
                next_gen = []
                for component, signal_received,sender in this_gen:
                    if component == "rx" and signal_received == 0:
                        return click
                    if component not in circuit_layout:
                        pass
                    elif circuit_layout[component][0] == 0:
                        for next_component in circuit_layout[component][1]:
                            low += 1
                            next_gen.append((next_component, 0, component))
                    elif ((circuit_layout[component][0] == 1 or
                           circuit_layout[component][0] == 2)
                          and signal_received == 0):
                        signal_to_send = 1 if circuit_layout[component][0] == 1 else 0
                        flip_or_flop = 2 if circuit_layout[component][0] == 1 else 1
                        circuit_layout[component] = (flip_or_flop,
                                                     circuit_layout[component][1])

                        for next_component in circuit_layout[component][1]:
                            high += 1 if signal_to_send else 0
                            low += 1 if not signal_to_send else 0
                            next_gen.append((next_component, signal_to_send, component))

                    elif circuit_layout[component][0] == 3 :
                        
                        conjun_mem[component][sender] = signal_received
                        
                        signal_to_send = 0 if set(conjun_mem[component].values()) == {1} else 1
                        
                        for next_component in circuit_layout[component][1]:
                            high += 1 if signal_to_send else 0
                            low += 1 if not signal_to_send else 0
                            next_gen.append((next_component, signal_to_send,component))
            # print((low,high))     
            current_cir_layout = tuple(circuit_layout.items())
            if current_cir_layout in cycle_detection:
                final_gen.append((current_cir_layout,(click+1, (low, high))))
                break
            cycle_detection[current_cir_layout] = (click+1, (low, high))
            click_to_circ[click+1] = current_cir_layout

        # print(circuit_layout)
        # print(cycle_detection)
        # print(final_gen)
        if final_gen:
            start_of_cycle = cycle_detection[final_gen[0][0]][0]
            end_of_cycle = final_gen[0][1][0]
            cycle_length = end_of_cycle-start_of_cycle
            
            cycle, remainder = divmod((NUM_OF_CLICKS-start_of_cycle),cycle_length)
            
            ans = 0
            # pre-cycle
            lowsum = 0
            highsum = 0
            for click in range(start_of_cycle+1):
                lowsum += cycle_detection[click_to_circ[click]][1][0]
                highsum += cycle_detection[click_to_circ[click]][1][1]
            
            cl_sum = 0
            ch_sum = 0
            
            # cycle
            for click in range(start_of_cycle+1,end_of_cycle):
                cl_sum += cycle_detection[click_to_circ[click]][1][0]
                ch_sum += cycle_detection[click_to_circ[click]][1][1]
            cl_sum += final_gen[0][1][1][0] 
            ch_sum += final_gen[0][1][1][1]
            lowsum += cl_sum*cycle
            highsum += ch_sum*cycle
            
            # after-cycle
            for click in range(start_of_cycle+1,start_of_cycle+1+remainder):
                lowsum += cycle_detection[click_to_circ[click]][1][0]
                highsum += cycle_detection[click_to_circ[click]][1][1]
            return lowsum*highsum
        else:
            # no cycle found!
            ans = 0
            lowsum = 0
            highsum = 0
            for _,info in cycle_detection.items():
                lowsum += info[1][0]
                highsum += info[1][1]
            ans = lowsum*highsum
            return ans

            
                

if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = simulate_circuit(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The area of this map is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
