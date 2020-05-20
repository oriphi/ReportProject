# Number of operations: 2* n ** 3 
# Use a Roofline Plot using operation per cycles instead of flops
# OpenMp
## 15 x 15
  - Single Thread     : 39820
  - Parallel no DMA   : 12079
  - Parallel DMA      : 12985
  - Parallel DMA  SVM : 13036

## 20 x 20
  - Single Thread     : 92650
  - Parallel no DMA   : 24750
  - Parallel DMA      : 23318
  - Parallel DMA  SVM : 25596

## 25 x 25
  - Single Thread     : 179030
  - Parallel no DMA   :  38090
  - Parallel DMA      :  39568
  - Parallel DMA  SVM :  39415

## 30 x 30
  - Single Thread     : 307210
  - Parallel no DMA   :  59887
  - Parallel DMA      :  61701
  - Parallel DMA  SVM :  61635

## 35 x 35
  - Single Thread     : 485440
  - Parallel no DMA   :  89283
  - Parallel DMA      :  91754
  - Parallel DMA  SVM :  61682


# 40 x 40
  - Single Thread     : 721970
  - Parallel no DMA   : 126523
  - Parallel DMA      : 129668
  - Parallel DMA  SVM : 129413

# Halide
## 15x15
	- Base                     : 40628 cycles
	- Parallel (y)             : 6950 cycles
	- Parallel(y) Vectorize(x) : 4339 cycles

## 20x20
	- Base                     : 93818 cycles
	- Parallel(y)              : 15585 cycles
	- Parallel(y) Vectorize(x) : 8358  cycles
## 25x25
	- Base                     : 180686 cycles
	- Parallel(y)              : 30413  cycles
	- Parallel(y) Vectorize(x) : 15585  cycles


## 30x30
	- Base                      : 309426 cycles
	- Parallel(y)               :  42659 cycles
	- Parallel(y) Vectorize(x,8) :  18776 cycles

## 35x35
	- Base                     : 488316 cycles
	- Parallel(y)              :  71279 cycles
	- Parallel(y) Vectorize(x) :  32295 cycles

## 40x40
	- Base                     : 725606 cycles
	- Parallel(y)              :  92536 cycles
	- Parallel(y) Vectorize(x) :  36487 cycles

