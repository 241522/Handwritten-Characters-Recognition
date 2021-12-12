import { useState } from "react";

import ImageDrop from "./components/ImageDrop";
import Options from "./components/Options";
import Results from "./components/Results";

function App() {
  const [path, setPath] = useState();
  const [loaded, setLoaded] = useState();
  const [dataPresent, setDataPresent] = useState(false);
  const [data, setData] = useState();

  return (
    <div className="main">
      <ImageDrop
        loaded={loaded}
        setLoaded={(load) => setLoaded(load)}
        path={path}
        setPath={(path) => setPath(path)}
      />

      {loaded && (
        <div className="results-container">
          <Options
            path={path}
            setDataPresent={(ans) => setDataPresent(ans)}
            setData={(data) => setData(data)}
          />
          {dataPresent && <Results data={data} />}
        </div>
      )}
    </div>
  );
}

export default App;
