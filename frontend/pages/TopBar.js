import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import HomeFeed from './homefeed';
import Messages from './messages';
import Profile from './profile';
import Link from 'next/link';

function TopBar() {
    return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light w-100 d-flex justify-content-center" style={{ paddingLeft: '20px', paddingRight: '20px' }}>        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
            <div className="navbar-nav">
            <Link href="/homefeed" className="nav-link">
                Home<span className="sr-only">(current)</span>
            </Link>
            <Link href="/profile" className="nav-link">
                Profile
            </Link>
            <Link href="/messages" className="nav-link">
                Messages
            </Link>
            </div>
        </div>
        <a className="navbar-brand mx-auto" href="#">The Social Network</a>
        </nav>
    );
}

export default TopBar;