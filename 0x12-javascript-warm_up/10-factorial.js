
#!/usr/bin/node
const my_Arg = process.argv.slice(2);
function factorial (num) {
  if (isNaN(my_Arg[0])) {
    return 1;
  }
  if (num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(parseInt(my_Arg[0])));
