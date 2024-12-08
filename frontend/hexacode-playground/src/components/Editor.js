import React from "react";

function Editor({ script, setScript }) {
  return (
    <textarea
      value={script}
      onChange={(e) => setScript(e.target.value)}
      placeholder="// Écrivez votre code HexaCode ici..."
      rows="10"
      cols="50"
    ></textarea>
  );
}

export default Editor;
