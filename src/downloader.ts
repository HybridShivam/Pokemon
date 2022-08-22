import axios from "axios";
import fs from "fs";
import { pad } from "./util";

const file = fs.readFileSync("urls.json");

if (!file) {
  console.log("No file found");
  process.exit(1);
}

const urls = JSON.parse(file.toString()) as {
  name: string;
  url: string;
  id: number;
}[];

const fetchImage = (url: string) =>
  axios.get<any>(url, {
    responseType: "stream",
    validateStatus(status) {
      return true;
    },
  });

const sleep = (ms: number) => {
  var start = new Date().getTime(),
    expire = start + ms;
  while (new Date().getTime() < expire) {}
  return;
};

const getImage = async (url: string, path: string): Promise<fs.WriteStream> => {
  const response = await fetchImage(url);
  if (response.status === 503) {
    console.log("Got 503 on", path);
    sleep(1000);
    return getImage(url, path);
  } else {
    return response.data.pipe(fs.createWriteStream(path));
  }
};

async function main() {
  if (!fs.existsSync("./assets")) fs.mkdirSync("./assets");
  if (!fs.existsSync("./assets/normal")) fs.mkdirSync("./assets/normal");
  for (const url of urls) {
    let form = "";
    // TODO: use ids instead of names
    const name = url.name;
    if (name.split("-").length > 1) {
      form = name.split("-").slice(1).join("-");
      if (
        // fix conflicts in names like ho-oh becomes [id]-oh because it thinks ho is a form
        form === "Oh" ||
        form === "Mime" ||
        form === "Null" ||
        form === "Jr." ||
        form === "Rime" ||
        form === "Z" || // Porygon-Z
        form === "o" // Kommo-o jangmo-o etc
      )
        form = "";

      form = form.replace("Gigantamax", "Gmax");
      name.startsWith("Tapu") ? (form = "") : "";
    }

    const stream = await getImage(
      url.url,
      `./assets/normal/${pad(url.id)}${form ? "-" + form : ""}.png`
    );

    stream.on("finish", () => console.log("Finished", url.name));
  }
}

main();
