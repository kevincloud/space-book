const user = {
    key: 'f2a04a9b-8e6f-4684-8da3-38e8dfda38cd',
    custom: {
        'user-type': 'beta',
        'location': 'GA'
    }
};
const client = LDClient.initialize('63249c64bbbf43110a181f46', user);

client.on('change', (settings) => {
    console.log('flags changed:', settings);
    if (settings.newLayout) {
        var origLayout = document.getElementById("original-layout");
        var newLayout = document.getElementById("new-layout");
        if (settings.newLayout.current) {
            origLayout.style.display = "none";
            newLayout.style.display = "block";
        } else {
            newLayout.style.display = "none";
            origLayout.style.display = "block";
        }
    }

    if (settings.enableRatings) {
        var newRatings = new Array();
        var oldLikes = new Array();
        var elements = document.getElementsByTagName("div");
        for (element of elements) {
            if (element.id == "new-ratings") {
                newRatings.push(element);
            }
            if (element.id == "old-likes") {
                oldLikes.push(element);
            }
        };
        console.log("ids: ", newRatings);
        if (settings.enableRatings.current) {
            oldLikes.forEach(element => {
                element.style.display = "none";
            });
            newRatings.forEach(element => {
                element.style.display = "block";
            });
        } else {
            newRatings.forEach(element => {
                element.style.display = "none";
            });
            oldLikes.forEach(element => {
                element.style.display = "block";
            });
        }
    }

    if (settings.headingColor) {
        const colormap = {
            'light-blue': 'has-background-info',
            'light-green': 'has-background-primary',
            'red': 'has-background-danger',
            'blue': 'has-background-link',
            'green': 'has-background-success',
            'gray': 'has-background-grey-light'
        }

        var headers = new Array();
        var oldValue = settings.headingColor.previous;
        var newValue = settings.headingColor.current;
        var elements = document.getElementsByTagName("div");
        for (element of elements) {
            if (element.id == "main-header") {
                headers.push(element);
            }
        };

        headers.forEach(element => {
            element.classList.remove(colormap[oldValue]);
            element.classList.add(colormap[newValue]);
        });
    }
});
  