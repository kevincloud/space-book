const user = {
    key: 'webapp-demo',
    name: 'Kevin Cochran'
};
const client = LDClient.initialize('62b0f22b8fc16e15a42d77d2', user);

client.on('change', (settings) => {
    console.log('flags changed:', settings);
    location.reload();
});
  