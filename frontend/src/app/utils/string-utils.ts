export function getSmartArticle(word: string): string {
  if (!word) return 'a';

  const lowercase = word.toLowerCase();

  const hardU = ['unicorn', 'university', 'unilateral', 'usual'];
  const hardO = ['one', 'once'];
  const hardE = ['european', 'eulogy'];
  const silentH = ['honest', 'honor', 'hour', 'heir'];

  if (hardU.includes(lowercase) || hardO.includes(lowercase) || hardE.includes(lowercase)) return 'A';
  if (silentH.includes(lowercase)) return 'An';

  return /^[aeiou]/.test(lowercase) ? 'An' : 'A';
}