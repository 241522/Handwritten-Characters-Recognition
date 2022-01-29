import { useState, useEffect } from "react";
import Drop from "./images/drop.svg";

const fs = window.require("fs");
// const pathModule = window.require("path");

const imageTypes = [
  "image/png",
  "image/jpeg",
  "image/ico",
  "image/tiff",
  "image/gif",
];

function ImageDrop({ loaded, setLoaded, path, setPath, moreThanOne }) {
  const [image, setImage] = useState();
  const [imageDispl, setImageDispl] = useState();
  const [errMsg, setErrMsg] = useState();

  useEffect(() => {
    moreThanOne(image?.length > 1);
  }, [image?.length, moreThanOne]);

  const onDropEvent = (e) => {
    e.stopPropagation();
    e.preventDefault();
    try {
      let filesObj = e.dataTransfer.files;
      let files = Object.keys(filesObj).map((key) => filesObj[key]);
      let fileTypes = files.map((file) => file.type);
      fileTypes.forEach((fileType) => {
        let tmp = imageTypes.some((type) => type === fileType);
        if (!tmp) throw new Error("Wrong file type!");
      });
      setImage(files);
      setPath(files.map((file) => file.path));
      let _img = files.map((file) =>
        fs.readFileSync(file.path).toString("base64")
      );
      setImageDispl(_img);
      setErrMsg(null);
      setLoaded(true);
    } catch (er) {
      setErrMsg(er.message);
      setLoaded(false);
    }
  };

  return (
    <div
      className="container center"
      style={{
        width: loaded && "50%",
        height: loaded ? "fit-content" : "100%",
        maxHeight: "100%",
        borderStyle: loaded && "solid",
      }}
      onDragOver={(e) => {
        e.stopPropagation();
        e.preventDefault();
      }}
      onDrop={(e) => {
        onDropEvent(e);
      }}
    >
      {loaded ? (
        <div className="images-container">
          {imageDispl?.map((filePath, key) => (
            <img
              key={key}
              src={`data:${image[key].type};base64,` + filePath}
              style={{
                width: image.length > 1 ? "100%" : "calc(50vw - 30px)",
              }}
              alt=""
            />
          ))}
        </div>
      ) : (
        <div>
          <img src={Drop} alt="" />
          <div className="error">{errMsg}</div>
        </div>
      )}
    </div>
  );
}

export default ImageDrop;
