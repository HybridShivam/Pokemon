import { JSDOM } from "jsdom";
import axios from "axios";
import fs from "fs";

import { pad, capitalize } from "./util";

async function main() {
  const pollyfills = {
    "Eiscue-Noice": "https://bulbapedia.bulbagarden.net/wiki/File:HOME875N.png",
    "Darmanitan-Galar-Zen":
      "https://bulbapedia.bulbagarden.net/wiki/File:HOME555GZ.png",
    "Zarude-Dada": "https://bulbapedia.bulbagarden.net/wiki/File:HOME893D.png",
    "Eternatus-Eternamax":
      "https://bulbapedia.bulbagarden.net/wiki/File:HOME890E.png",
    "Mimikyu-Busted":
      "https://bulbapedia.bulbagarden.net/wiki/File:HOME778B.png",
    "Magearna-Original":
      "https://bulbapedia.bulbagarden.net/wiki/File:HOME801O.png",
    "Cramorant-Gulping":
      "https://bulbapedia.bulbagarden.net/wiki/File:HOME845Gu.png",
    "Cramorant-Gorging":
      "https://bulbapedia.bulbagarden.net/wiki/File:HOME845Go.png",
  };
  const {
    data: { results },
  } = await axios.get<{ results: { name: string; url: string }[] }>(
    "https://pokeapi.co/api/v2/pokemon?limit=100000"
  );
  const urls: { url: string; name: string; id: number }[] = [];
  for (const result of results) {
    result.name = result.name.split("-").map(capitalize).join("-");
    result.name.includes("Urshifu-Single-Strike-Gmax")
      ? (result.name = "Urshifu-Gigantamax Single Strike")
      : null;
    result.name.includes("Urshifu-Rapid-Strike-Gmax")
      ? (result.name = "Urshifu-Gigantamax Rapid Strike")
      : null;
    result.name.includes("Toxtricity-Amped-Gmax")
      ? (result.name = "Toxtricity-Gigantamax")
      : null;
    result.name.includes("Toxtricity-Low-Key-Gmax")
      ? (result.name = "Toxtricity-Gigantamax")
      : null;
    result.name.includes("Nidoran") ? (result.name = "nidoran") : "";
    result.name.includes("Farfetch")
      ? (result.name = result.name.replace("Farfetchd", "Farfetch'd"))
      : "";
    result.name.includes("Sirfetch") ? (result.name = "Sirfetch'd") : "";

    result.name.replaceAll("-Own-Tempo", "");
    result.name.replaceAll("Morpeko-Full-Belly", "Morpeko");
    result.name.includes("Mr-Mime")
      ? (result.name = result.name.replace("Mr-Mime", "Mr. Mime"))
      : "";
    result.name.includes("Mr-Rime")
      ? (result.name = result.name.replace("Mr-Rime", "Mr. Rime"))
      : "";
    result.name.includes("Mime-Jr")
      ? (result.name = result.name.replace("Mime-Jr", "Mime Jr."))
      : "";

    result.name.includes("Deoxys-Normal") ? (result.name = "Deoxys") : "";

    result.name.includes("Minior") ? (result.name = "Minior") : "";

    result.name.includes("Flabebe") ? (result.name = "Flabébé") : "";
    result.name.startsWith("Tapu-")
      ? (result.name = result.name.replaceAll("-", " "))
      : "";
    /(jangmo|hakamo|kommo)-o/gi.test(result.name)
      ? (result.name = result.name.replace(/\-O/gi, "-o"))
      : "";

    result.name.includes("Basculin")
      ? (result.name = result.name.replaceAll("-Striped", ""))
      : "";
    result.name = result.name.replaceAll("-Standard", "");
    result.name = result.name.replaceAll("Calyrex-Ice", "Calyrex-Ice Rider");
    result.name = result.name.replaceAll(
      "Calyrex-Shadow",
      "Calyrex-Shadow Rider"
    );

    if (result.name === "Zygarde-50-Power-Construct") continue;
    if (result.name === "Zygarde-10-Power-Construct")
      result.name = "Zygarde-10";

    result.name = result.name.replaceAll("-Incarnate", "");
    result.name = result.name.replaceAll(/-(Large|Super|Small)/gi, "");
    result.name = result.name.replaceAll("Mega-X", "Mega X");
    result.name = result.name.replaceAll("Mega-Y", "Mega Y");
    result.name = result.name.replaceAll("-Eternal", "");
    result.name = result.name.replaceAll("-Ordinary", "");
    result.name = result.name.replaceAll("-Aria", "");
    result.name = result.name.replaceAll("-Average", "");
    result.name = result.name.replaceAll("-Midday", "");
    result.name = result.name.replaceAll("-Low-Key", "-Low Key");
    result.name = result.name.replaceAll("Mimikyu-Disguised", "Mimikyu");
    result.name = result.name.replaceAll("-50", "");
    result.name = result.name.replaceAll("-10", "-10Percent");
    result.name = result.name.replaceAll("%", "Percent");
    result.name = result.name.replaceAll("-Strike", " Strike");
    result.name = result.name.replaceAll("Strike-", "Strike ");
    result.name = result.name.replaceAll("Type-", "Type ");
    result.name = result.name.replaceAll("-Gmax", "-Gigantamax");
    result.name = result.name.replaceAll("-Star", " Star");
    result.name = result.name.replaceAll("-Full-Belly", "-Full");
    result.name = result.name.replaceAll("-Cap", "");
    result.name = result.name.replaceAll("-Power-Construct", "Percent");
    result.name = result.name.replaceAll("-Pau", "-Pa'u");
    result.name = result.name.replaceAll("Necrozma-Dusk", "Necrozma-Dusk Mane");
    result.name = result.name.replaceAll(
      "Necrozma-Dawn",
      "Necrozma-Dawn Wings"
    );
    result.name = result.name.replaceAll("Dawn-", "Dawn ");
    result.name = result.name.replaceAll("-Phd", "-PhD");
    result.name = result.name.replaceAll("-Crowned", "");
    // replace zacian and zamazenta with zacian-crowned and zamazenta-crowned if its not already crowned
    result.name = result.name.replaceAll(
      /zacian(?!\-crowned)/gi, // NOT already crowned
      "Zacian-Hero"
    );
    result.name = result.name.replaceAll(
      /zamazenta(?!\-crowned)/gi, // NOT already crowned
      "Zamazenta-Hero"
    );

    if (result.name === "Greninja-Battle-Bond") continue;
    if (result.name === "Rockruff-Own-Tempo") continue;
    if (result.name.includes("-Totem")) continue;
    if (result.name === "Magearna-Original") continue;
    if (
      ["Pikachu Starter", "Pikachu-Cosplay", "Eevee Starter"].includes(
        result.name
      )
    )
      continue;

    // remove trailing slash
    if (result.url.endsWith("/")) result.url = result.url.slice(0, -1);

    let id = Number(result.url.split("/").pop());

    if (id > 1000) {
      const { data } = await axios.get<any>(result.url); // forms
      let url = data.species.url;
      if (url.endsWith("/")) url = url.slice(0, -1);
      id = Number(url.split("/").pop());
    }
    let url =
      "https://bulbapedia.bulbagarden.net/wiki/File:" +
      pad(id) +
      capitalize(result.name).trim() +
      ".png";

    // check for pollyfills
    Object.keys(pollyfills).includes(result.name)
      ? (url = pollyfills[result.name])
      : "";

    console.log(result.name, id, url);

    const { window } = await JSDOM.fromURL(url);
    const document = window.document;
    const link = document.querySelector("#file > a");
    urls.push({
      name: result.name.replaceAll(" ", "-").replaceAll('."', ""),
      url: "https:" + link.getAttribute("href"),
      id,
    });
  }
  fs.writeFileSync("urls.json", JSON.stringify(urls, null, 2));
}

main();
