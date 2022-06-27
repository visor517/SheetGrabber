export default function Row({ item }) {
    return (
        <tr>
            {Object.values(item).map((value,val_i) => <td key={val_i}>{String(value)}</td>)}
        </tr>
    )
}