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
    const name = url.name;
    if (name.split("-").length > 1) {
      // do [id]-[form] stuff here
    }
    const stream = data.pipe(
      fs.createWriteStream("assets/" + url.name + ".png")
    );

    stream.on("finish", () => console.log(url.name));
  }
}

main();
