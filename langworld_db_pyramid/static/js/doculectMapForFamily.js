import getLocale from "./tools/getLocale.js";
import MapAndList from "./map/MapAndList.js";

let splitURL = location.pathname.split("/");
const indexOfFamilyID = splitURL.indexOf("family") + 1;
const familyID = splitURL[indexOfFamilyID];

ReactDOM.render(
  React.createElement(MapAndList, {
    mapDivID: "map-default",
    urlToFetch: `/${getLocale()}/json_api/doculects_for_map/family/${familyID}`,
  }),
  document.getElementById("map-and-list")
);
