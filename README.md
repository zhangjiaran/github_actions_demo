# github_actions_demo

This repository contains GitHub Actions workflow examples.

## Hello World Compile and Debug Action

This repository includes a simple C "Hello World" program and a GitHub Actions workflow that demonstrates:

- **Compilation**: Compiles the hello_world.c program using GCC
- **Execution**: Runs the compiled program  
- **Debugging**: Uses GDB to debug the program with breakpoints
- **Binary Analysis**: Shows information about the compiled binary

### Files

- `hello_world.c` - A simple C program that prints "Hello, World!"
- `.github/workflows/hello-world-compile-debug.yml` - GitHub Actions workflow for compilation and debugging

### Workflow Triggers

The workflow runs on:
- Push to main/master branches
- Pull requests to main/master branches
- Manual trigger (workflow_dispatch)

### Running Locally

To compile and run the program locally:

```bash
gcc -g -o hello_world hello_world.c
./hello_world
```

To debug with GDB:

```bash
gdb ./hello_world
```