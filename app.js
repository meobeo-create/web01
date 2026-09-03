fetch ("https://jsonplaceholder.typicode.com/users " )
    .then (function(response ) {
        return response.json () ;
    })
    .then (function(data) {
        console.log(data) ; // parsed array of users
    })
    .catch(function(error) {
        console.error("Something went wrong :",error) ;
    }) ;

// 1. Simulate network delay with setTimeout wrapped in a Promise
function fetchData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("Data successfully retrieved!");
    }, 2000); // 2-second delay
  });
}

// 2a. Call it using .then() chaining
fetchData()
  .then((data) => {
    console.log("Using .then():", data);
  })
  .catch((error) => {
    console.error("Error:", error);
  });

// 2b. Call it using async/await
async function runAsync() {
  try {
    const data = await fetchData();
    console.log("Using async/await:", data);
  } catch (error) {
    console.error("Error:", error);
  }
}

runAsync();