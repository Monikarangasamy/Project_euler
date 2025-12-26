const fs = require('fs');

function solveNamesScores(filePath) {
  const rawData = fs.readFileSync(filePath, 'utf8');
  const names = rawData.replace(/"/g, '').split(',').sort();

  let totalScore = 0;

  for (let i = 0; i < names.length; i++) {
    const name = names[i];
    let alphabeticalValue = 0;

    for (let j = 0; j < name.length; j++) {
      alphabeticalValue += (name.charCodeAt(j) - 64);
    }
    const nameScore = alphabeticalValue * (i + 1);
    totalScore += nameScore;
  }
  return totalScore;
}
const result = solveNamesScores('0022_names.txt');
console.log('The total of all name scores is:', result);