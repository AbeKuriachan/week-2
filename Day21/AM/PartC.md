# Week 04 · Day 21 AM — Part C: Interview Ready (Written Answers)

Code for Q2 and Q3 speedup demo is in `AM_PartC_Code.py`.

---

## Q1 — What is NumPy Broadcasting? Why is it useful?

Broadcasting is NumPy's mechanism for performing arithmetic between arrays of
different shapes without copying data.

**The 3 rules (applied right-to-left on shapes):**
1. If arrays differ in number of dimensions, prepend `1`s to the smaller shape.
2. Dimensions of size `1` are stretched to match the other array.
3. If two dimensions are unequal and neither is `1`, broadcasting fails.

**Why useful:** You can add a bias vector to every row of a matrix, scale columns
by different factors, or normalize an entire dataset — all in one line with no
loops and no wasted memory copies.

---

## Q3 — Vectorisation vs Loops: Why is NumPy Faster?

**Python loops** execute inside the interpreter. Each iteration carries:
- Python object creation per element
- Dynamic type checking
- Interpreter bytecode dispatch overhead

**Vectorisation** pushes the entire operation into pre-compiled C/Fortran that
uses SIMD (Single Instruction, Multiple Data) CPU instructions — one instruction
processes 4–16 numbers simultaneously on contiguous memory blocks.

Rule of thumb: if you write `for i in range(len(arr))` on a NumPy array,
there is almost always a one-line vectorised alternative.
