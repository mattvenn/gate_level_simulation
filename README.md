# Gate Level Simulation

Simulation normally means using a tool like iverilog or verilator to run a simulation of your hardware design.
Neither of these tools are doing synthesis to end up with the actual hardware that will be used on an FPGA or an ASIC.

Gate level simulation is done by synthesising the design into the gates that are used in the final FPGA or ASIC and then 
using a lower level 'behavioural' model for each of the types of gates or standard cells.

With OpenLANE, we take the post synthesis netlist from Yosys and use this as the gate level netlist. Using the behavioural models
from the Skywater PDK we can then run a simulation that is closer to the hardware.

# Instructions

Run `make` to run the simulation. Then `make show` to show the waves with GTKWave. Check the Makefile to see how it's done.

For your own simulations using the open PDK you'll need to add these lines to your post synthesis netlist:

    `define UNIT_DELAY #1
    `define USE_POWER_PINS
    `define FUNCTIONAL
    `include "libs.ref/sky130_fd_sc_hd/verilog/primitives.v"
    `include "libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v"

If you have an issue with syntax errors in the behavioural Verilog, it's most likely due to these bugs:

* https://github.com/google/skywater-pdk/issues/297
* https://github.com/google/skywater-pdk/issues/292

The `define FUNCTIONAL takes care of 292. 297 is fixed in a more recent PDK, and you can easily fix it by commenting out the 2 bad lines in sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v

Search for: 

    wire 1
