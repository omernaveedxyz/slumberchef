import type { APIRoute } from "astro";

export const GET: APIRoute = ({ redirect }) => {
  return redirect("/");
};

export const POST: APIRoute = async ({ redirect, request }) => {
  try {
    const data = await request.formData();
    var object: { [key: string]: number } = {};
    data.forEach((value, key) => (object[key] = parseInt(value.toString())));
    return redirect(
      `/results/${Buffer.from(JSON.stringify(object)).toString("base64url")}`,
    );
  } catch (error) {
    if (error instanceof Error) {
      console.error(error.message);
    }
    return redirect("/");
  }
};
