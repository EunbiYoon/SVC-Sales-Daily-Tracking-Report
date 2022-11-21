// node to run python
const spawner=require('child_process').spawn;

// //string
// const data_to_pass_in='Send this to python script.';
// console.log('Data sent to python script:', data_to_pass_in);
// const python_process=spawner('python',['./python.py',data_to_pass_in]);
// python_process.stdout.on('data',(data) => {
//   console.log('Data received from python script: ',data.toString());
// });


//array
const data_to_pass_in=['Send this to python script.'];
console.log('Data sent to python script:', data_to_pass_in);
const python_process=spawner('python',['./python.py',JSON.stringify(data_to_pass_in)]);
python_process.stdout.on('data',(data) => {
  console.log('Data received from python script: ',JSON.parse(data.toString()));
});