import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles

async def activate_project(dut, number, compare):
    # reset it
    dut.la_data_in <= (1 << 25)
    await ClockCycles(dut.wb_clk_i, 1)
    dut.la_data_in <= 0
    await ClockCycles(dut.wb_clk_i, 1)

    # load a smaller value
    dut.la_data_in <= compare + (1 << 24)
    await ClockCycles(dut.wb_clk_i, 1)
    dut.la_data_in <= 0


@cocotb.test()
async def test_tri(dut):
    clock = Clock(dut.wb_clk_i, 10, units="ns")
    cocotb.fork(clock.start())
    dut.VGND <= 0
    dut.VPWR <= 1
    dut.active <= 0 # outputs tristated to start with

    dut.wb_rst_i <= 1
    await ClockCycles(dut.wb_clk_i, 5)
    dut.wb_rst_i <= 0
    dut.la_data_in <= 0

    await ClockCycles(dut.wb_clk_i, 10)

    # activate proj0
    await activate_project(dut, 0, 1)
    dut.active <= 1 # turn on outputs

    await ClockCycles(dut.wb_clk_i, 100)
