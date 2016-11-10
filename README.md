# 16 Segment Decoder
MSI circuit to decode six binary bits into an alphanumeric character on a sixteen segment display

###Circuit Design Process:

* A [555 timer](http://www.ti.com/lit/ds/symlink/lm555.pdf) generates a 1 Hz clock
* The generated wave is fed into an 8-bit binary counter
 * 8-bit counter made by cascading two [74LS168 4-bit counters](http://www.ece.usu.edu/ece_store/spec/74168_74169-16p.pdf)
* Output bits are fed into a series of three [GAL22V10 PLDs](http://web.mit.edu/6.115/www/document/gal22v10.pdf), programmed using CUPL
* PLDs output appropriate SOPs for each of the segments on the [sixteen segment display](http://www.foryard-led.ru/pdf/fys-15012ax_bx.pdf)

###Logic Design Process:

* Truth table values are determined in an Excel spreadsheet
* Unsimplified SOP boolean equations are generated by the spreadsheet
* Equations simplified using the software [Logic Friday](http://www.sontrak.com/)
* Simplified equations parsed by a Python script and outputted in CUPL syntax
* PLDs are given I/O pin assignments and programmed using [WinCUPL](http://www.atmel.com/tools/WINCUPL.aspx)
* Compiled `.jed` files are burned to PLDs

Project for ECET10. Schematic designed with [Multisim](http://www.ni.com/multisim/).


