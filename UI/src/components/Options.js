import axios from "axios";

function Options({ path, setDataPresent, setData }) {
  const sendPath = async () => {
    try {
      let tmp = await axios.post("http://127.0.0.1:5000/image", {
        path: path,
      });
      console.log(tmp);
      if (tmp.data) {
        setDataPresent(true);
        setData(tmp.data);
      }
    } catch (er) {
      console.log(er);
    }
  };
  return (
    <div className="options">
      <div className="choices">Deep Learning</div>
      <div className="proc-button center" onClick={() => sendPath()}>
        Process
      </div>
    </div>
  );
}

export default Options;
