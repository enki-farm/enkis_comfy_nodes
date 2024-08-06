import { app } from "../../scripts/app.js";

function debounce(func, delay) {
    let debounceTimer;
    return function () {
        const context = this;
        const args = arguments;
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => func.apply(context, args), delay);
    };
}

const ext = {
    name: "enki.seaboard_reader",
    nodeCreated(node) {
        console.log("node created", node);

        if (node.comfyClass !== "enki.seaboard.reader") return;

        var script = document.createElement('script');
        script.src = 'extensions/enkis_comfy_nodes/mpe.min.js';
        document.head.appendChild(script);

        script.addEventListener('load', function () {
            console.log("script injected");

            const instrument = window.mpe();

            navigator.requestMIDIAccess().then(access => {
                // Iterate over the list of inputs returned
                access.inputs.forEach(midiInput => {
                    console.log(midiInput);

                    // only listen to the seaboard check if lower name contains seaboard
                    if (!midiInput.name.toLowerCase().includes("seaboard")) return;

                    midiInput.addEventListener(
                        'midimessage',
                        (event) => instrument.processMidiMessage(event.data)
                    );
                });

                // Subscribe to instrument changes and update the HTML element
                instrument.subscribe(debounce((change) => {
                    if (change.length === 0) return;

                    // round the value to 2 decimal places
                    let cur_value = Math.round(change[0][node.widgets[0].value] * 100) / 100 * 2;

                    if (cur_value === node.widgets_values[2]) return;

                    node.widgets[2].value = cur_value;
                    node.widgets[1].value = change[0].noteNumber;
                    node.setDirtyCanvas(true);
                    app.queuePrompt();

                }, 100));
            });
        });
    }
};

app.registerExtension(ext);