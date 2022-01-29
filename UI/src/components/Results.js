import { useState } from "react";
import Clip from "./images/clipboard-data.svg";
import Close from "./images/x-lg.svg";

function Results({ name, data, stats = null }) {
  const [showStats, setShowStats] = useState(false);
  return (
    <code className="results">
      <div className="inside">
        {name}
        {data?.map((pred, id) => (
          <ul key={id}>
            <li>filename: {pred?.filename}</li>
            <li>character: {pred?.character}</li>
            <li>label: {pred?.label}</li>
          </ul>
        ))}
      </div>
      {stats && (
        <div className={"stats " + (showStats ? "widen" : "")}>
          {!showStats ? (
            <img
              className="ico"
              src={Clip}
              alt=""
              onClick={() => setShowStats(true)}
            />
          ) : (
            <code>
              {Object.keys(stats).map(
                (stat, i) =>
                  stat !== "predictions" && (
                    <div key={i}>
                      {stat.replace("_", " ") + ": " + stats[stat]}
                    </div>
                  )
              )}
              <img
                className="ico pointer"
                src={Close}
                alt=""
                onClick={() => setShowStats(false)}
              />
            </code>
          )}
        </div>
      )}
    </code>
  );
}

export default Results;
