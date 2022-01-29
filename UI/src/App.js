import { useState } from "react";

import ImageDrop from "./components/ImageDrop";
import Options from "./components/Options";
import Results from "./components/Results";

const dummyStats = {
  stats_nn: {
    accuracy: 0.1,
    time: 0,
    labeled_count: 1,
    total_count: 10,
    average_time: 0.0,
    predictions: [
      {
        filename: "LABEL_4_obrazekblabla.png",
        character: "4",
        label: null,
      },
      {
        filename: "test_image2.png",
        character: "Y",
        label: null,
      },
      {
        filename: "test_image3.png",
        character: "P",
        label: null,
      },
      {
        filename: "test_image4.png",
        character: "a",
        label: null,
      },
    ],
  },

  stats_fb: {
    accuracy: 0.1,
    time: 0,
    labeled_count: 1,
    total_count: 10,
    average_time: 0.0,
    predictions: [
      {
        filename: "LABEL_4_obrazekblabla.png",
        character: "4",
        label: null,
      },
      {
        filename: "test_image2.png",
        character: "Y",
        label: null,
      },
      {
        filename: "test_image3.png",
        character: "P",
        label: null,
      },
      {
        filename: "test_image4.png",
        character: "a",
        label: null,
      },
    ],
  },
};

function App() {
  const [path, setPath] = useState();
  const [loaded, setLoaded] = useState();
  const [dataPresent, setDataPresent] = useState(false);
  const [data, setData] = useState(dummyStats);
  const [moreThanOne, setMoreThanOne] = useState(false);

  return (
    <div className="main">
      <div className="titlebar" />
      <ImageDrop
        loaded={loaded}
        setLoaded={(load) => setLoaded(load)}
        path={path}
        setPath={(path) => setPath(path)}
        moreThanOne={(isMore) => setMoreThanOne(isMore)}
      />

      {loaded && (
        <div className="results-container">
          {dataPresent && (
            <Results
              name="Deep Learning"
              data={data?.stats_nn?.predictions}
              stats={data?.stats_nn}
            />
          )}
          {dataPresent && (
            <Results
              name="Feature Based"
              data={data?.stats_fb?.predictions}
              stats={data?.stats_fb}
            />
          )}

          <Options
            path={path}
            setDataPresent={(ans) => setDataPresent(ans)}
            setData={(data) => setData(data)}
            moreThanOne={moreThanOne}
          />
        </div>
      )}
    </div>
  );
}

export default App;
