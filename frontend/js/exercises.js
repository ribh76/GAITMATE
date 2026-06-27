import { getLatestRisk } from "./api.js";
import { tintForColor } from "./risk.js";

const liveValue = document.querySelector("[data-live-value]");
const liveLabel = document.querySelector("[data-live-label]");
const liveBar = document.querySelector("[data-live-bar]");

if (liveValue && liveLabel && liveBar) {
  getLatestRisk()
    .then(({ overall }) => {
      liveValue.textContent = overall.score;
      liveLabel.textContent = overall.label;
      liveLabel.style.color = overall.color;
      liveLabel.style.background = tintForColor(overall.color);
      liveBar.style.width = `${overall.score}%`;
      liveBar.style.color = overall.color;
    })
    .catch(() => {
      liveLabel.textContent = "Backend offline";
    });
}
