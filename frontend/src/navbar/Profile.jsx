import { useState, useEffect } from "react";

function Profile() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/profiles/")
      .then((response) => response.json())
      .then((data) => setUsers(data))
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-indigo-950 py-16 px-6">

      <h1 className="text-center text-5xl font-extrabold bg-gradient-to-r from-cyan-400 via-purple-500 to-pink-500 bg-clip-text text-transparent mb-14">
        User Profiles
      </h1>

      <div className="max-w-6xl mx-auto grid gap-10 sm:grid-cols-2 lg:grid-cols-3">

        {users.map((user) => (
          <div
            key={user.id}
            className="group relative overflow-hidden rounded-3xl border border-white/10 bg-white/10 backdrop-blur-xl p-8 shadow-2xl transition-all duration-500 hover:-translate-y-3 hover:shadow-cyan-500/30"
          >
            {/* Gradient Glow */}
            <div className="absolute -top-16 -right-16 h-40 w-40 rounded-full bg-cyan-500/20 blur-3xl group-hover:bg-purple-500/30 transition-all"></div>

            <div className="relative flex flex-col items-center">

              <img
                src={`http://127.0.0.1:8000${user.profile_pic}`}
                alt={user.username}
                className="h-36 w-36 rounded-full border-4 border-cyan-400 object-cover shadow-xl transition duration-500 group-hover:scale-105"
              />

              <h2 className="mt-6 text-3xl font-bold text-white">
                {user.username}
              </h2>

              <p className="mt-1 text-cyan-300">
                Student Profile
              </p>

              <div className="mt-8 w-full space-y-4">

                <div className="rounded-xl bg-white/5 p-4 border border-white/10">
                  <p className="text-sm text-gray-400">📧 Email</p>
                  <p className="mt-1 break-all text-white font-medium">
                    {user.email}
                  </p>
                </div>

                <div className="rounded-xl bg-white/5 p-4 border border-white/10">
                  <p className="text-sm text-gray-400">📱 Phone</p>
                  <p className="mt-1 text-white font-medium">
                    {user.phone_number}
                  </p>
                </div>

                <div className="rounded-xl bg-white/5 p-4 border border-white/10">
                  <p className="text-sm text-gray-400">📝 Bio</p>
                  <p className="mt-1 text-gray-200 leading-relaxed">
                    {user.bio}
                  </p>
                </div>

              </div>

            

            </div>
          </div>
        ))}

      </div>
    </div>
  );
}

export default Profile;