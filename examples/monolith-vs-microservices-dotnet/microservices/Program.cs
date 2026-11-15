using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace microservices
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureServices((hostContext, services) =>
                {
                    services.AddOrleans();
                })
                .UseOrleansHosting();
    }
}

namespace microservices
{
    public static class OrleansExtensions
    {
        public static IHostBuilder AddOrleans(this IHostBuilder builder)
        {
            // Фиктивная реализация
            return builder;
        }

        public static IHostBuilder UseOrleansHosting(this IHostBuilder builder)
        {
            // Фиктивная реализация
            return builder;
        }
    }
}