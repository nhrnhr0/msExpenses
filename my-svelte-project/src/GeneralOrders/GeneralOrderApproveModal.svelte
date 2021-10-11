
<script>
    //export let itemId;
    import { getContext } from 'svelte';
    const { close } = getContext('simple-modal');

    export let onOkey;
    function approve() {
        onOkey();
        close()
    }
</script>

<div class="text">
    האם אתה בטוח שברצונך לאשר?
</div>
<div class="buttons">
    <button on:click|preventDefault={approve}>כן</button>
</div>
