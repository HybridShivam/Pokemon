import axios from "axios";
import fs from "fs";

const file = fs.readFileSync("urls.json");

if (!file) {
  console.log("No file found");
  process.exit(1);
}

const urls = JSON.parse(file.toString()) as { name: string; url: string }[];

async function main() {
  for (const url of urls) {
    const { data } = await axios.get<any>(url.url, {
      responseType: "stream",
    });
    let form = "";
    const name = url.name;
    if (name.split("-").length > 1) {
      form = name.split("-").slice(1).join("-");
    }
    const stream = data.pipe(
      fs.createWriteStream("assets/" + name + form + ".png")
    );

    stream.on("finish", () => console.log(url.name));
  }
}

main();
