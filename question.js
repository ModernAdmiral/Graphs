// Print each element on own line in alphabetical order

// sort array
// loop though array
// console.log each element

arr = [
  "Waltz",
  "Tango",
  "Viennese Waltz",
  "Foxtrot",
  "Cha Cha",
  "Samba",
  "Rumba",
  "Paso Doble",
  "Jive",
];

const sortAndPrintArr = (arr) => {
  arr = arr.sort();
  arr.forEach((e) => {
    console.log(e);
  });
};

sortAndPrintArr(arr);
