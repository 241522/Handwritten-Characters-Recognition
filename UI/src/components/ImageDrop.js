import { useState } from "react";
import Drop from "./images/drop.svg";

const fs = window.require("fs");
// const pathModule = window.require("path");

function ImageDrop({ loaded, setLoaded, path, setPath }) {
  const [image, setImage] = useState();
  const [imageDispl, setImageDispl] = useState();

  return (
    <div
      className="container center"
      style={{
        width: loaded && "50%",
        height: loaded ? "fit-content" : "100%",
        borderStyle: loaded && "solid",
      }}
      onDragOver={(e) => {
        e.stopPropagation();
        e.preventDefault();
      }}
      onDrop={(e) => {
        e.stopPropagation();
        e.preventDefault();
        try {
          setImage(e.dataTransfer.files[0]);
          setPath(e.dataTransfer.files[0].path);
          let _img = fs
            .readFileSync(e.dataTransfer.files[0].path)
            .toString("base64");
          setImageDispl(_img);
          setLoaded(true);
        } catch (er) {
          console.log(er);
          setLoaded(false);
        }
      }}
    >
      {loaded ? (
        <img
          src={`data:${image.type};base64,` + imageDispl}
          style={{ width: "calc(50vw - 30px)", objectFit: "contain" }}
          alt=""
        />
      ) : (
        <img src={Drop} alt="" />
      )}
    </div>
  );
}

export default ImageDrop;
