//lab1
// 1. Model a list of prediction samples [{id, name, result}]
const predictions = [
  { id: 1, name: "Sample A", result: "Positive", score: 85 },
  { id: 2, name: "Sample B", result: "Negative", score: 42 },
  { id: 3, name: "Sample C", result: "Positive", score: 91 },
  { id: 4, name: "Sample D", result: "Negative", score: 67 },
  { id: 5, name: "Sample E", result: "Positive", score: 78 }
];

//Write a for loop that filters the array by a condition
const positivePredictions = [];
for (let i = 0; i < predictions.length; i++) {
  if (predictions[i].result === "Positive") {
    positivePredictions.push(predictions[i]);
  }
}
console.log("Filtered Predictions (Positive):", positivePredictions);

// Write a function that sums a numeric field across all objects
function sumNumericField(array, fieldName) {
  let total = 0;
  for (let i = 0; i < array.length; i++) {
    total += array[i][fieldName];
  }
  return total;
}
console.log("Total Score:", sumNumericField(predictions, "score"));

//Write a function that finds the object with the largest value of a field, using a for loop
function findMaxByField(array, fieldName) {
  if (array.length === 0) return null;
  
  let maxObject = array[0];
  for (let i = 1; i < array.length; i++) {
    if (array[i][fieldName] > maxObject[fieldName]) {
      maxObject = array[i];
    }
  }
  return maxObject;
}
console.log("Prediction with Max Score:", findMaxByField(predictions, "score"));

// Convert one function to an arrow function
const sumNumericFieldArrow = (array, fieldName) => {
  return array.reduce((sum, item) => sum + item[fieldName], 0);
};
console.log("Total Score (Arrow Function):", sumNumericFieldArrow(predictions, "score"));

//lab2
const form = document.getElementById("house-price-form");
const messageContainer = document.getElementById("message-container");

// Attach addEventListener("submit", ...) và call event.preventDefault()
form.addEventListener("submit", function(event) {
  event.preventDefault();

  // Clear the previous error before showing a new one
  messageContainer.innerHTML = "";

  const location = document.getElementById("location").value.trim();
  const bedroomsInput = document.getElementById("bedrooms").value.trim();
  const bedrooms = Number(bedroomsInput);

  let errorMessage = "";

  // Check required fields are not empty, and "bedrooms" is a positive number
  if (location === "" || bedroomsInput === "") {
    errorMessage = "All fields are required!";
  } else if (isNaN(bedrooms) || bedrooms <= 0) {
    errorMessage = "Bedrooms must be a positive number!";
  }

  if (errorMessage !== "") {
    // On failure: create a red <p> error with createElement()/appendChild()
    const errorP = document.createElement("p");
    errorP.style.color = "red";
    errorP.textContent = errorMessage;
    messageContainer.appendChild(errorP);
  } else {
    // On success: display a "Ready to submit" message
    const successP = document.createElement("p");
    successP.style.color = "green";
    successP.textContent = "Ready to submit";
    messageContainer.appendChild(successP);
  }
});

//TUAN4

//Lab1
// 1. Simulate network delay with setTimeout() wrapped in a Promise
function simulateNetworkRequest() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const isSuccess = true; // Giả lập trạng thái thành công
      if (isSuccess) {
        resolve("Dữ liệu đã được tải thành công");
      } else {
        reject("Lỗi: Không thể kết nối tới máy chủ.");
      }
    }, 2000); 
  });
}

// 2a. Call it once using .then()
console.log("--- Gọi bằng .then() ---");
simulateNetworkRequest()
  .then((data) => {
    console.log("Kết quả (.then):", data);
  })
  .catch((error) => {
    console.error("Lỗi (.then):", error);
  });

// 2b. Call it once using async/await
async function handleAsyncRequest() {
  try {
    const data = await simulateNetworkRequest();
    console.log("Kết quả (async/await):", data);
  } catch (error) {
    console.error("Lỗi (async/await):", error);
  }
}

handleAsyncRequest();

