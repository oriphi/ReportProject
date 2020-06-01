# Review Presentation
# Monday 08 / 06 / 2020 : 16h

- Change the title of the project
- Add Matheus, Luca, Samuel
- Use the Eth template (maybe ...), or use a better template
		Use: ETH Zürich ASL Presentation Template (Overleaf) 
		Change the Asl Logo
- CHANGE TO POWERPOINT


# Heterogeneous Systems
- Catchy intro !!
~30 sec on why het systems work !!

Can be *bolder* with the structure -> Don't spend too much time on general stuff
- They know about heterogeneous systems -> Don't waste time on it

	Second or third slide: See the motivations of the project
		Implementing image processing pipeline sucks on hero -> we need Halide to solve our issues.

::::::::::::::::::::::::::::::::::::::::::::::
::  Go to the motivation quite fast         ::
::  Convice people to listen at my work !!! ::
::::::::::::::::::::::::::::::::::::::::::::::

Pitch Idea:
===========

```
Switch to open office for presentation.

GOTTA GO FAST : 2-3 slides, situation, problem, solution
First slide use anchor to start 
; Stay general!!

Halide is better for image processing workflow ... Otherwise destroyed by OpenMP
Slide 1:
--------
Heterogeneous system good for image processing
Example: Smartphone process 4K raw image process
	- SoC: not good enough
	- Heterogeneous systems

	What's the problem
    -------------------
	Programing PMCA = Hard
	Lot of accelerators, need to optimize for each of them tedious ...

Slide 2:
	Solution:
    ---------
	 Halide -> GENERAL presentation
	 	Separt function / processing
		Only write the processing part once
		Writting schedule made easier.

Slide 3:
--------
	In my work I want to test Halide
	enable Halide in the hero platform
# Talk about the  project
	Enable Halide on the Hero platform.

Slide 4:
--------
	Hero platform
	What is hero ? Open Source Hete plat developed here at iis

Slide 5:
--------
	Halide language
	First we need to really talk about Halide to see if it really is a solution



Slide 6:
  --------
	Comparaison Halide / OpenMp -> longer version of the start of the presentation
	Left Column:
		Halide code + schedule separated
	Right Column:
		OpenMp -> highlight the schedule (implement a more complex schedule)

Slide 7:
--------
	Keep var x,a, matrix_mul, out -> do not need to compile

	Algorithm -> Agnostic no architecture information
		Use Animations hide the code to focus on the elements I am talking about
		Use colors
		Shorten the code
	Schedule:
		Ton of schedules, 
		3 schedules: parallel, vecctorize, tile
		Get the gifs from the tutorial

Slide 8: Implementation
--------
	Implementing the runtime
	Making Halide works on HERO
		Halide expects some functions to parallelize code

Slide 9:
--------
	~ 30 s
	`Explained more in depth in the report`
	The Compilation Process
		Compilation Flow figure added in the report
	

Slide 10:
---------
		Test setup
		1 slide on methodology
		What am I doing, How did I get those results

Slide 11:
---------
	Halide results

	For image processing comparable results
	- Compare performance AND programming model
		For this simple exmaple -> the same as 1 pragma for parallelization

Slide 12:
---------
	Rise of the Performance

	Not much effort  from the programmer side
	How easy it was to test the schedule
	The final best performance

	Don't talk about the automated tool (keep it to next)
		Not available on RISC-V ...


Slide 13:
---------
	Next Step, Additional effort
	Halide cool for image processing, but big downsize: ease of programming for hetero systems.
	Not available
		But suggestions on how this  can be implemented

	-> Automated scheduler: Make the process even easier
Slide 14:
---------
	Conclusion:
	wrap things up
		Did it work or not?
	
	Thanks / Good Bye
```
