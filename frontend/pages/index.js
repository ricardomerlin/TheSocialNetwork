import Head from 'next/head';
import "bootstrap/dist/css/bootstrap.min.css";
import Link from 'next/link';
import TopBar from './TopBar';

function Home() {
  return (
    <div>
      <Head>
        <title>The Social Network</title>
        <link rel="icon" href="/TheSocialNetworkLogo.png" />
      </Head>

      <main className='main-container'>
        <TopBar />
      </main>

      <footer>

      </footer>
    </div>
  );
}

export default Home;