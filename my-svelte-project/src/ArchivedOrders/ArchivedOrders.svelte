<script>
    import Modal from 'svelte-simple-modal';
    import SvelteTooltip from 'svelte-tooltip';
    
    import {
        Circle
    } from 'svelte-loading-spinners'
    import {
        onMount
    } from 'svelte'
    let all_rows_data = [];
    let BASE_API_URL = '/api/archived/'
    let query = BASE_API_URL;
    let sortBy = {col: "created", ascending: true};
    $: sort = (column) => {
		
		if (sortBy.col == column) {
			sortBy.ascending = !sortBy.ascending
		} else {
			sortBy.col = column
			sortBy.ascending = true
		}
		
		// Modifier to sorting function for ascending or descending
		let sortModifier = (sortBy.ascending) ? 1 : -1;
		
		let sort = (a, b) => 
			(a[column] < b[column]) 
			? -1 * sortModifier 
			: (a[column] > b[column]) 
			? 1 * sortModifier 
			: 0;
		
        all_rows_data = all_rows_data.sort(sort);
	}

    function get_from_server() {
        var requestOptions = {
            method: 'GET',
            redirect: 'follow'
        };

        fetch(query, requestOptions)
            .then(response => response.json())
            .then(result => {
                console.log('got result: ', result);
                all_rows_data = result;
                refreshing = false;
            })
            .catch(error => {
                console.log('error', error)
                refreshing = false;
            });
    }
    function refresh_from_server() {
        refreshing = true;
        get_from_server();
    }
    let refreshing = false;
    onMount(() => {
        console.log('onMount');
        refreshing = true;
        get_from_server();
    })

</script>

<div class="buttons">
    
    <button on:click|preventDefault="{refresh_from_server}">    
        {#if refreshing}
            <Circle size="30" color="#FF3E00" unit="px" duration="1s"></Circle>
        {:else}
            רענן
        {/if}
    </button>
</div>
הזמנות:

<table id="table">
    <tr>
        <th class:sorted="{sortBy['col'] == 'id'}" on:click={sort("id")}>
            id
        </th>
        <th class:sorted="{sortBy['col'] == 'created'}" on:click={sort("created")}>
            תאריך
        </th>
        <th class:sorted="{sortBy['col'] == 'name'}" on:click={sort("name")}>
            תיאור רכישה
        </th>
        <th class:sorted="{sortBy['col'] == 'providerName'}" on:click={sort("providerName")}>
            ספק
        </th>
        <th class:sorted="{sortBy['col'] == 'total'}" on:click={sort("total")}>
            סכום כולל מע"מ
        </th>
        <th class:sorted="{sortBy['col'] == 'type'}" on:click={sort("type")}>
            סוג הוצאה
        </th>
        <th class:sorted="{sortBy['col'] == 'invoiceNumber'}" on:click={sort("invoiceNumber")}>
            מספר קבלה
        </th>
        <th class:sorted="{sortBy['col'] == 'paidHow'}" on:click={sort("paid")}>
            שולם?
        </th>
        <th class:sorted="{sortBy['col'] == 'paidHow'}" on:click={sort("paidHow")}>
            איך שולם
        </th>
        <th class:sorted="{sortBy['col'] == 'whenToPay'}" on:click={sort("whenToPay")}>
            מתי שולם
        </th>
        <th class:sorted="{sortBy['col'] == 'invoiceLocation'}" on:click={sort("invoiceLocation")}>
            מיקום חשבונית
        </th>
    </tr>
    {#each all_rows_data as row} 
        <tr>
            <td>{row.id}</td>
            <td>{new Date(row.created).toLocaleString('he-IL', {timeZone:'Asia/Jerusalem'})}</td>
            
            
            <td>{row.name}</td>
            <td>{row.providerName}</td>
            <td>{row.total}</td>
            <td>{row.type}</td>
            <td>{row.invoiceNumber}</td>
            <td>{row.paid?"כן":"לא"}</td>
            <td>{row.paidHow}</td>
            <td>{new Date(row.whenToPay).toLocaleDateString('he-IL', {timeZone:'Asia/Jerusalem'})}</td>
            <td>{row.invoiceLocation}</td>
        </tr>
    {/each}
</table>



<style lang="scss">
    .buttons {
        min-height: 150px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    table {
        width: 100%;
        border: 1px solid black;

        margin-bottom: 150px;
    }
    #table {
        font-family: Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 100%;
        & td, & th {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        & tr:nth-child(even){background-color: #f2f2f2;}
        & tr:hover {background-color: #ddd;}
        & th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: right;
            background-color: #04AA6D;
            color: white;
            &.sorted {
                border: 1px solid red;
            }
        }
    }   
</style>
