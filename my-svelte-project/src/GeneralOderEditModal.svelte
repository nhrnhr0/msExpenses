<script>
    export let itemId;
    let name_input_value;
    let provider_input_value;
    let total_input_value;
    let type_input_value;

    function can_save(name, provider, total, type) {
        console.log('type: ',type);
        if(name && type) {
            return true
        }return false;
    }
    $: can_svave_reactive = can_save(name_input_value,provider_input_value,total_input_value,type_input_value);

</script>


<h1>בקשת הזמנת רכש</h1>
<form action="http://127.0.0.1:8000/api/general/" method="POST">
    <div class="form-group">
        <label for="name">שם:</label>
        <input type="text" name="name" bind:value={name_input_value}>
    </div>
    <div class="form-group">
        <label for="provider">ספק:</label>
        <input type="text" name="provider" bind:value={provider_input_value}>
    </div>
    <div class="form-group">
        <label for="total">עלות:</label>
        <input type="text" name="total" bind:value={total_input_value}>
    </div>
    <div class="form-group">
        <label for="type">סוג רכישה:</label>
        <select name="type" bind:value={type_input_value}> 
            <option value=""></option>
            <option value="CO">קבועות</option>
            <option value="AC">רכש</option>
            <option value="PR">ספקים</option>
        </select>
    </div>

    {#if can_svave_reactive}
        <button>save</button>
    {/if}
</form>