import { useState } from "react";

import axios from "axios";

function Options({ path, setDataPresent, setData, moreThanOne }) {
  const [error, setError] = useState(false);
  const [loading, setLoading] = useState(false);
  // const [checks, setChecks] = useState({ deep: false, feature: false });

  const sendPath = async () => {
    setLoading(true);
    try {
      let tmp = await axios.post(
        "http://127.0.0.1:8000/images/",
        {
          path: path,
        },
        { headers: { "content-type": "application/json" } }
      );
      if (tmp?.data) {
        setError(false);
        setDataPresent(true);
        setData(tmp.data);
      }
    } catch (er) {
      setError(true);
    }
    setLoading(false);
  };
  return (
    <div className="options">
      {/* <div className="choices">
        <label className="check-container">
          Deep Learning
          <input
            type="checkbox"
            checked={checks.deep}
            onChange={() => setChecks({ ...checks, deep: !checks.deep })}
          />
          <span className="checkmark"></span>
        </label>

        <label className="check-container">
          Feature Based
          <input
            type="checkbox"
            checked={checks.feature}
            onChange={() => setChecks({ ...checks, feature: !checks.feature })}
          />
          <span class="checkmark"></span>
        </label>
      </div> */}
      <div className="proc-button center" onClick={() => sendPath()}>
        {loading ? <div className="loading" /> : "Process"}
      </div>
      {error && <div className="error">Connection Error</div>}
    </div>
  );
}

export default Options;
