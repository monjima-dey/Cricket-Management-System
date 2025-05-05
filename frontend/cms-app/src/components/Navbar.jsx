import React from 'react';

const navLinks = [
  { label: 'Home', href: '/' },
  { label: 'Matches', href: '/' },
  { label: 'Tournaments', href: '/' },
  { label: 'Login', href: '/' },
];

const NavLink = ({ label, href }) => {
  return (
    <li>
      <a href={href} className="hover:underline">
        {label}
      </a>
    </li>
  );
};

const Navbar = () => {
  return (
    <nav className="bg-blue-900 text-white px-6 py-4 flex justify-between items-center">
      <h1 className="text-xl font-bold">Cricket Management</h1>
      <ul className="flex gap-6">
        {navLinks.map((link) => (
          <NavLink key={link.label} label={link.label} href={link.href} />
        ))}
      </ul>
    </nav>
  );
};

export default Navbar;