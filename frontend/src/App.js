import './App.css';
import Sidebar from './components/Sidebar';
import 'bootstrap/dist/css/bootstrap.min.css';
import {useState, useEffect} from 'react';

function App() {
  const [searchText, setSearchText] = useState("");

  const getCurrentDate=() => {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //As January is 0.
    var yyyy = today.getFullYear();
    
    if(dd<10) dd='0'+dd;
    if(mm<10) mm='0'+mm;
    return (`${mm}/${dd}/${yyyy}`);
  }

  useEffect(() => {
    loadMap()
  }, [searchText])

  const loadMap = () => {
    document.getElementById("map-container").innerHTML = '<object class="map-view" type="text/html" data="Map.html" ></object>';
  }

  return (
    <div className="App">
      <section className="app-header">
        <h1>App name</h1>
        <p>{getCurrentDate()}</p>
      </section>
      <main className="row main-view p-2">
        <section className="col-sm-12 col-md-8">
        <div className="input-group mb-2">
          <input type="search" className="form-control rounded" placeholder="Search" aria-label="Search" id="search-input"
          aria-describedby="search-addon" />
          <button type="button" className="btn btn-outline-primary" onClick={() => setSearchText(document.getElementById("search-input").value)}>search</button>
        </div>
        <div className="map-view" id="map-container"></div>
        </section>
        <section className="col-sm-12 col-md-4">
        <Sidebar />
        </section>
      </main>
    </div>
  );
}

export default App;
