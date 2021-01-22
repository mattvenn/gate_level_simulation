# cocotb setup
export COCOTB_REDUCED_LOG_FMT=1
MODULE = test_wrapper
TOPLEVEL = wrapper
VERILOG_SOURCES = wrapper.lvs.powered.v

COMPILE_ARGS=-I /home/matt/work/asic-workshop/pdks/sky130A/ -DSIM -DFUNCTIONAL -DMPRJ_IO_PADS=38    

include $(shell cocotb-config --makefiles)/Makefile.sim
