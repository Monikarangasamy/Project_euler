function sumSquareDifference() {
    const n = 100;
    const squareOfSum = ((n * (n + 1)) / 2) ** 2;
    const sumOfSquare = (n * (n + 1) * (2 * n + 1)) / 6;
    return squareOfSum - sumOfSquare;
}

console.log(sumSquareDifference());