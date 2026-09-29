export default function ReferenceTables() {
  return (
    <>
      <table className="ref-table">
        <thead>
          <tr>
            <th></th>
            <th>m</th>
            <th>f</th>
            <th>n</th>
            <th>pl</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td className="case-label">Nom.</td>
            <td>der</td>
            <td>die</td>
            <td>das</td>
            <td>die</td>
          </tr>
          <tr>
            <td className="case-label">Akk.</td>
            <td>den</td>
            <td>die</td>
            <td>das</td>
            <td>die</td>
          </tr>
          <tr>
            <td className="case-label">Dat.</td>
            <td>dem</td>
            <td>der</td>
            <td>dem</td>
            <td>den (+n)</td>
          </tr>
          <tr>
            <td className="case-label">Gen.</td>
            <td>des</td>
            <td>der</td>
            <td>des</td>
            <td>der</td>
          </tr>
        </tbody>
      </table>

      <div className="sidebar-title">Pronouns</div>
      <table className="ref-table">
        <thead>
          <tr>
            <th>Nom.</th>
            <th>Akk.</th>
            <th>Dat.</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>ich</td>
            <td>mich</td>
            <td>mir</td>
          </tr>
          <tr>
            <td>du</td>
            <td>dich</td>
            <td>dir</td>
          </tr>
          <tr>
            <td>er</td>
            <td>ihn</td>
            <td>ihm</td>
          </tr>
          <tr>
            <td>sie</td>
            <td>sie</td>
            <td>ihr</td>
          </tr>
          <tr>
            <td>es</td>
            <td>es</td>
            <td>ihm</td>
          </tr>
          <tr>
            <td>wir</td>
            <td>uns</td>
            <td>uns</td>
          </tr>
          <tr>
            <td>ihr</td>
            <td>euch</td>
            <td>euch</td>
          </tr>
          <tr>
            <td>sie/Sie</td>
            <td>sie/Sie</td>
            <td>ihnen/Ihnen</td>
          </tr>
        </tbody>
      </table>
    </>
  );
}
