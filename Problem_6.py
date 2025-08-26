def sum_square_difference():
    n = 100
    square_of_sum = ((n * (n + 1)) // 2) ** 2
    sum_of_square = (n * (n + 1) * (2 * n + 1)) // 6
    return square_of_sum - sum_of_square

print(sum_square_difference())

#solved in javascript

function sumSquareDifference() {
    const n = 100;
    const squareOfSum = ((n * (n + 1)) / 2) ** 2;
    const sumOfSquare = (n * (n + 1) * (2 * n + 1)) / 6;
    return squareOfSum - sumOfSquare;
}

console.log(sumSquareDifference());


