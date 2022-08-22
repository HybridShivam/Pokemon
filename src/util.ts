export function pad(number: number | string, length = 3) {
  let str = "" + number;
  while (str.length < length) {
    str = "0" + str;
  }
  return str;
}

export const capitalize = (string: string) =>
  string.charAt(0).toUpperCase() + string.slice(1);
