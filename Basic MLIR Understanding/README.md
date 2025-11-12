# Take Home Assignment

This take home assignment is for evaluating your ability to build LLVM/MLIR, read MLIR, diagnose syntax issues, run core lowering passes, and produce a native binary.

**What you'll submit**: A short report (`REPORT.md`) and generated artifacts(files).


## 1. Build the LLVM toolchain (with MLIR included)

MLIR is a project under the LLVM compiler toolchain. It lets you define domain-specific operations in modular dialects, then progressively lower them to various abstraction levels.
We will be using `mlir-opt`, a tool provided by the MLIR project under the llvm compiler toolchain.

1. Clone the `llvm-project` from the `llvm` organization.
   - references:
       - https://releases.llvm.org/18.1.8/docs/GettingStarted.html#checkout-llvm-from-git
       - https://github.com/llvm/llvm-project
1. Use the latest `20.x release` version.
1. Compile the llvm toolchain with mlir project included.

While following the instructions above please provide the following information in your report:

1. The exact tag and the full commit SHA you used to build the llvm toolchain. (Use git or any other tool to get the information)
1. The commands you used to compile the mlir toolchain. (If there are certain options you had used, please explain why you used them)
1. Location of the binaries you have compiled.


## 2. Detect the syntax error within the `example.mlir` file.

1. Use the `mlir-opt` binary to detect the syntax error

Add the information below in the report:

1. The Error message of the syntax error.
1. The reason why the syntax was wrong.


## 3. Apply passes

Apply the passes below
1. `one-shot-bufferize` with additional attributes: bufferize-function-boundaries(should be set to `1`), function-boundary-type-conversion(should be set to `identity-layout-map`). The resulting artifact should be saved in a file named `example.bufferized.mlir`.
1. `convert-linalg-to-loops`. The resulting artifact should be saved in a file named `example.loops.mlir`.
1. `convert-bufferization-to-memref`. The resulting artifact should be saved in a file named `example.nobuf.mlir`.
1. `convert-scf-to-cf`. The resulting artifact should be saved in a file named `example.cf.mlir`.
1. `convert-to-llvm`. The resulting artifact should be saved in a file named `example.llvm.mlir`.

Please provide the result of each passes in separate files. The name of the files should be distinguishable to the pass applied before. (Try mixing up the order of the passes and see what happens. It will be subject to a plus point.)

## 4. Convert the MLIR IR to LLVM IR 

The final result of the previous step is an mlir ir in a LLVM Dialect. Now convert this mlir ir to a llvm ir.

Look for the appropriate tool in the binaries you have compiled in step 1 to convert the mlir ir to llvm ir. (Try converting other artifacts you have created in the previous steps and see what happens. It will be subject to a plus point.)

## 5. Generate an executable
From the final llvm ir, compile to whichever backend(cpu) compatible binary you have. The name of the binary should be `final`. It is ok if you run into a segmentation fault when you run the executable. (Digging for the reason of the segmentation fault and adding it to your report will be subject to a plus point)

- You might need to compile `clang` from the llvm compiler toolchain codebase you've used for compiling llvm and mlir in the previous steps due to compatibility issues.


Please provide the information of your backend like the information below:
```
❯ uname -m
x86_64
```


## Friendly Note: 
If you get stuck in one of the steps above, don’t worry. Please conduct a thorough analysis of any errors you've encountered and document your findings in the report; this analysis will be evaluated as part of your score.
